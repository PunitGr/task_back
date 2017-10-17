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
 role | String ("R"/"A")
 
    
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
    "id": 2,
    "firstName": "Punit",
    "lastName": "Grover",
    "phoneNumber": "+919911138192",
    "email": "groove679@gmail.com",
    "role": "R"
}
```

<br/>

#### 2. For deleting a Team Member
 
* **Request URL:**

    `DELETE` `/users/<pk>` 


* **Query Parameters:**

Parameter | Type
:------------: | :-------------:
 id | Primary Key

<br/>

#### 3. For editing a Team Member's info
 
* **Request URL:**

    `PATCH` `/users/<pk>/` 


* **Query Parameters:**

Parameter | Type
:------------: | :-------------:
 id | Primary Key


* **Request:**

```javascript
{
    "firstName": "Test"
}
```


* **Response:**

```javascript
{
    "firstName": "Test"
}
```

<br/>

#### 4. Get all team members details
 
* **Request URL:**

    `GET` `/users/` 


* **Response:**

```javascript
[
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

```

<br/>

#### 5. Get team member by Primary Key
 
* **Request URL:**

    `GET` `/users/<pk>` 

* **Query Parameters:**

Parameter | Type
:------------: | :-------------:
 id | Primary Key


* **Response:**

```javascript
{
    "id": 1,
    "firstName": "Test",
    "lastName": "Jones",
    "phoneNumber": "+9198921138142",
    "email": "test@gmail.com",
    "role": "Regular"
}
```

<br/>
