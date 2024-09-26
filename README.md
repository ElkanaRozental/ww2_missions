
### required installs

````bash
pip install Flask psycopg2 returns SQLAlchemy typing 
````

### load app.py

````python
app = Flask(__name__)

if __name__ == '__main__':
    create_tables()
    insert_data_from_unnormalized()

    app.register_blueprint(mission_blueprint, url_prefix="/api/mission")
    app.run(debug=True, use_reloader=False)
````