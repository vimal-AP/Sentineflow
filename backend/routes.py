from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas
from database import get_db
import math

router = APIRouter()

# 1. Route to Register a New Technician
@router.post("/technicians", response_model=schemas.TechnicianResponse, status_code=status.HTTP_201_CREATED)
def create_technician(tech: schemas.TechnicianCreate, db: Session = Depends(get_db)):
    db_tech = models.Technician(
        name=tech.name,
        phone=tech.phone,
        latitude=tech.latitude,
        longitude=tech.longitude
    )
    db.add(db_tech)
    db.commit()
    db.refresh(db_tech)
    return db_tech

# 2. Route to File a New Emergency Task
@router.post("/tasks", response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        latitude=task.latitude,
        longitude=task.longitude
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# 3. Route to Auto-Match and Dispatch the Closest Technician
@router.post("/tasks/{task_id}/dispatch")
def dispatch_task(task_id: int, db: Session = Depends(get_db)):
    # Fetch the task
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
        
    if task.status != "pending":
        return {"message": f"Task is already {task.status}", "assigned_technician_id": task.technician_id}

    # Fetch all available technicians who are online
    available_techs = db.query(models.Technician).filter(models.Technician.status == "available").all()
    if not available_techs:
        raise HTTPException(status_code=404, detail="No online technicians available right now")

    closest_tech = None
    shortest_distance = float('inf')

    # Basic Euclidean distance algorithm to calculate closest spatial coordinates
    for tech in available_techs:
        if tech.latitude is not None and tech.longitude is not None:
            distance = math.sqrt(
                (tech.latitude - task.latitude) ** 2 + 
                (tech.longitude - task.longitude) ** 2
            )
            if distance < shortest_distance:
                shortest_distance = distance
                closest_tech = tech

    if not closest_tech:
        raise HTTPException(status_code=400, detail="Available technicians do not have valid GPS coordinates")

    # Update database states: Assign tech to task, set statuses to busy/assigned
    task.technician_id = closest_tech.id
    task.status = "assigned"
    closest_tech.status = "busy"
    
    db.commit()

    return {
        "status": "Success",
        "message": f"Emergency '{task.title}' assigned to {closest_tech.name}",
        "assigned_technician": {
            "id": closest_tech.id,
            "name": closest_tech.name,
            "phone": closest_tech.phone
        }
    }
    from typing import List

# 4. Route to Get All Technicians (For Dashboard Monitoring)
@router.get("/technicians", response_model=List[schemas.TechnicianResponse])
def get_all_technicians(db: Session = Depends(get_db)):
    return db.query(models.Technician).all()

# 5. Route to Get All Tasks (To show incidents on a map dashboard)
@router.get("/tasks", response_model=List[schemas.TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

# 6. Route to Update Live GPS Coordinates of a Technician
@router.put("/technicians/{tech_id}/location")
def update_technician_location(tech_id: int, latitude: float, longitude: float, db: Session = Depends(get_db)):
    tech = db.query(models.Technician).filter(models.Technician.id == tech_id).first()
    if not tech:
        raise HTTPException(status_code=404, detail="Technician not found")
        
    tech.latitude = latitude
    tech.longitude = longitude
    db.commit()
    
    return {
        "message": f"Live location updated for {tech.name}",
        "current_location": {"latitude": latitude, "longitude": longitude}
    }