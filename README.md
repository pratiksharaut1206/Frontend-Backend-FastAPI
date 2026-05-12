## Execution flow

### Get Request Flow
1. User clicks the button.
2. Streamlit sends GET button
3. FastAPI receives the request
4. hello() function executes
5. Backend returns JSON
6. Streamlit displays message

### POST Request Flow

1. user enters name and clicks button
2. Streamlit will create JSON payload
3. The post request is send to backend
4. FASTAPI will validate JSON
5. greet_user() will be executed
6. JSON response is returned
7. Streamlit will display the result
