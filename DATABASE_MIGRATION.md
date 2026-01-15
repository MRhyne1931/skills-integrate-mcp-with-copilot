# Database Migration Guide

## Overview
This update migrates the Mergington High School application from in-memory storage to a persistent SQLite database using SQLAlchemy ORM.

## What Changed

### New Files
- **`database.py`**: Database configuration and session management
- **`models.py`**: SQLAlchemy models for Users, Activities, Events, and Clubs
- **`init_db.py`**: Database initialization script with seed data

### Modified Files
- **`app.py`**: Updated to use database instead of in-memory dictionary
- **`requirements.txt`**: Added SQLAlchemy and Alembic dependencies

## Database Schema

### Tables
1. **users**: Stores student and admin information
   - id, email, first_name, last_name, password_hash, role, created_at

2. **activities**: Stores extracurricular activities
   - id, name, description, schedule, max_participants, created_at

3. **activity_participants**: Many-to-many relationship between users and activities
   - activity_id, user_id, registered_at

4. **events**: For future time-based events (prepared for issue #10)
   - id, name, description, event_date, start_time, end_time, max_capacity, category, club_id

5. **clubs**: For future club management (prepared for issue #12)
   - id, name, description, category, contact_email, created_at

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Initialize Database
```bash
python src/init_db.py
```

This creates:
- SQLite database file: `mergington_high.db`
- All necessary tables
- Seed data from the original in-memory structure

### 3. Run the Application
```bash
uvicorn src.app:app --reload
```

## Benefits

✅ **Data Persistence**: Data survives server restarts
✅ **Scalability**: Ready for more complex queries and relationships
✅ **Foundation**: Enables authentication, events, clubs (issues #8, #10, #12)
✅ **Production Ready**: Can easily switch to PostgreSQL/MySQL
✅ **Data Integrity**: ACID compliance and referential integrity

## Environment Variables

- `DATABASE_URL`: Database connection string (default: `sqlite:///./mergington_high.db`)
  - For PostgreSQL: `postgresql://user:password@localhost/dbname`
  - For MySQL: `mysql://user:password@localhost/dbname`

## Migration Notes

- The API endpoints remain unchanged, ensuring backward compatibility
- Response format matches the original structure
- All existing functionality is preserved
- Database is automatically created on first run if it doesn't exist

## Future Enhancements

This database structure is designed to support:
- User authentication (issue #8)
- Event management with dates/times (issue #10)
- Club management system (issue #12)
- Role-based access control (issue #13)
- User profiles (issue #14)
