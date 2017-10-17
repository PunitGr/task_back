#### 1. For creating a Team Member
 
* **Request URL:**

    `POST` `/users/` 


* **Parameters:**

Parameter | Type
:------------: | :-------------:
 firstName | String
 lastName | String
 email | Email
 phoneNumber | Number
 role | String ("R"/A")
 
    
* **Request:**

```javascript
{   
    "firstName": "Punit",
    "lastName": "Grover",
    "phoneNumber": "+919911138192",
    "email": "groove679@gmail.com",
    "role": "R"
}
```


* **Response:**

```javascript
{
    "status": "success",
    "results": "Successfully created a team member"
}
```

<br/>

#### 2. For deleting a Team Member
 
* **Request URL:**

    `DELETE` `/users/?user=<id>` 


* **Query Parameters:**

Parameter | Type
:------------: | :-------------:
 user | id
 email | string 


* **Response:**

```javascript
{
    "status": "success",
    "results": "Successfully deleted a team member"
}
```

<br/>

#### 3. For editing a Team Member's info
 
* **Request URL:**

    `PATCH` `/users/edit/<user_id>/` 


* **Query Parameters:**

Parameter | Type
:------------: | :-------------:
 user_id | id


    
* **Request:**

```javascript
{
    "firstName": "Test"
}
```


* **Response:**

```javascript
{
    "status": "success",
    "results": {
        "firstName": "Test"
    }
}
```

<br/>

#### 4. Get all team members details
 
* **Request URL:**

    `GET` `/users/` 


* **Response:**

```javascript
{
    "status": "success",
    "results": [
        {
            "id": 1,
            "firstName": "Test",
            "lastName": "Jones",
            "phoneNumber": "+9198921138142",
            "email": "test@gmail.com",
            "role": "Regular"
        },
        {
            "id": 2,
            "firstName": "Punit",
            "lastName": "Jones",
            "phoneNumber": "+919821148142",
            "email": "gtest@gmail.com",
            "role": "Regular"
        }
    ]
}
```

<br/>

#### 5. Get team members by id or email
 
* **Request URL:**

    `GET` `/users/?user=1` 

* **Query Parameters:**

Parameter | Type
:------------: | :-------------:
 user | id
 email | Email


* **Response:**

```javascript
{
    "status": "success",
    "results": [
        {
            "id": 1,
            "firstName": "Test",
            "lastName": "Jones",
            "phoneNumber": "+9198921138142",
            "email": "test@gmail.com",
            "role": "Regular"
        }
    ]
}
```

<br/>
