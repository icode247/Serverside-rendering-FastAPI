# Server-side Rendering Application with FastAPI

This repository is a FastAPI application implementing server-side rendering.

## Folder Structure:

- `static`: This folder contains static files such as images, CSS stylesheets, and JavaScript files that are served by the application. These files are typically used to enhance the user interface of the web application.

- `templates`: This folder contains HTML templates that are used to render dynamic content in the web application. The templates typically use a templating engine like Jinja2 to include dynamic data in the HTML pages.

- `.gitignore`: This file specifies files and directories that should be excluded from version control when using Git. Typically, this includes files and directories that are specific to the development environment or contain sensitive information that should not be shared.

- `database.py`: This file contains code that interacts with a database. It typically defines functions or classes that handle database queries and updates.

- `main.py`: This file contains the main FastAPI application code. It defines the FastAPI instance and the endpoints of the application that handle HTTP requests and responses.

- `model.py`: This file contains code that defines the data model of the application. It typically defines classes that represent the data entities and their relationships.

- `requirements.txt`: This file lists the Python packages required by the application. It is used by package managers like pip to install the required packages.

- `schema.py`: This file contains code that defines the schema of the data entities used in the application. It typically defines classes that represent the schema of the data entities and their relationships.


## Run the Application:

Clone the repository:

    git clone https://github.com/icode247/Serverside-rendering-FastAPI/
    
Install the required dependencies:

    pip install -r requirements.txt
    
Start the FastAPI application:

    uvicorn main:app --reload

`main` is the name of the Python file containing the FastAPI application. 
`app` is the name of the FastAPI instance created in the Python file.
`--reload` flag enables auto-reloading of the server when changes are made to the code.

Open your web browser and navigate to http://localhost:8000/ to access the root endpoint of your FastAPI application.

Note: To access other endpoints in the FastAPI application, you can access them by appending the corresponding URL paths to http://localhost:8000/.

## Roadmap / TODO:

- Add more tests to ensure that the application functions correctly and handle errors and edge cases gracefully.
- Consider adding more security measures, such as authentication and authorization, to protect user data and prevent unauthorized access to the application.
- Add a database to the application
- Improve the performance of the application by optimizing database queries and reducing response times.
- Consider deploying the application to a cloud service like AWS or Google Cloud to make it more accessible and scalable.








