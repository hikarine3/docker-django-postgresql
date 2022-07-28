# v2.0.2
- Removed unnecessary debug information

# v2.0.1
- Force to use requirements.txt for creation of docker image instead of defining in Dockerfile
- Use hardlink for .env instead of symbolic link consideriong deployment
- Added not to use postgres user at the timing of creation of database

# v2.0.0
- Version up of software
  - OS: Alaminux instead of CentOS
  - Django 4.0 instead of Django 3.x
  - PostgreSQL 14 instead of PostgreSQL 12
- Adoption of .env instead of writing value directly in docker-compose.yml & settings.py
- Persistent data volume

# v1.6.0
Added some helpful functions for starting djang project to default status.
- User Authentification
- List page with pagination as example
- Data loader as example
- Responsive design
