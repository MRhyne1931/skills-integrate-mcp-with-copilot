"""
Database models for the application
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# Association table for many-to-many relationship between activities and participants
activity_participants = Table(
    'activity_participants',
    Base.metadata,
    Column('activity_id', Integer, ForeignKey('activities.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('registered_at', DateTime, default=datetime.utcnow)
)


class User(Base):
    """User model for storing student and admin information"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    password_hash = Column(String, nullable=True)  # For future authentication
    role = Column(String, default="student")  # student or admin
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    activities = relationship("Activity", secondary=activity_participants, back_populates="participants")


class Activity(Base):
    """Activity/Club model"""
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    schedule = Column(String, nullable=False)
    max_participants = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    participants = relationship("User", secondary=activity_participants, back_populates="activities")


class Event(Base):
    """Event model for time-based events"""
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    event_date = Column(DateTime, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    max_capacity = Column(Integer, nullable=False)
    category = Column(String, nullable=True)
    club_id = Column(Integer, ForeignKey('clubs.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Club(Base):
    """Club model for organizing groups"""
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=True)
    contact_email = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
