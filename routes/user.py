from fastapi import APIRouter,HTTPException, status
from models.user import User,Post ,Comment
from config.db import conn 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
router = APIRouter() 

@router.get('/users', tags=["Users"])
async def find_all_users():
    return serializeList(conn.local.user.find())


@router.post('/signup', tags=["Users"])
async def signup_user(user: User):
    user_dict = user.model_dump()  # Convert User object to a dictionary
    conn.local.user.insert_one(user_dict)
    return serializeList(conn.local.user.find())

@router.post('/login', tags=["Users"])
async def login_user(name: str, password: str):
    user = conn.local.user.find_one({"name": name})

    if user and user['password'] == password:
        # Authentication successful
        return {"message": "Login successful"}

    # If user doesn't exist or password is incorrect, raise HTTPException
    raise HTTPException(
        status_code=401,
        detail="Incorrect username or password"
    )

@router.put('/{id}', tags=["Users"])
async def update_user(id,user: User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@router.delete('/{id}', tags=["Users"])
async def delete_user(id,user: User):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))



# for posts

@router.get("/post/", tags=["Posts"])
async def find_all_posts():
    return serializeList(conn.local.post.find())

@router.post('/post/', tags=["Posts"])
async def create_post(post: Post):
    post_dict = post.model_dump()  # Convert Post object to a dictionary
    conn.local.post.insert_one(post_dict)
    return serializeList(conn.local.post.find())

@router.put('/post/{id}', tags=["Posts"])
async def update_post(id, post: Post):
    post_dict = post.model_dump(exclude_unset=True)  # Convert Post object to a dictionary
    conn.local.post.find_one_and_update({"_id": ObjectId(id)}, {"$set": post_dict})
    return serializeDict(conn.local.post.find_one({"_id": ObjectId(id)}))


@router.delete('/post/{id}', tags=["Posts"])
async def delete_post(id,post: Post):
    return serializeDict(conn.local.post.find_one_and_delete({"_id":ObjectId(id)}))


# For comments

@router.get("/post/comments/{id}", tags=["Comments"])
async def find_all_comments(id: str):
    return serializeList(conn.local.comment.find({"post": id}))


@router.post('/post/comments/{id}', tags=["Comments"])
async def create_comment(id,comment: Comment):
    comment.post=id
    comm_dict = comment.model_dump()  # Convert Post object to a dictionary
    conn.local.comment.insert_one(comm_dict)
    return serializeList(conn.local.comment.find())

@router.put('/post/comments/{id_comm}', tags=["Comments"])
async def update_comment(id_comm, comment: Comment):
    comm_dict = comment.model_dump(exclude_unset=True)  # Convert Post object to a dictionary
    conn.local.comment.find_one_and_update({"_id": ObjectId(id_comm)}, {"$set": comm_dict})
    return serializeDict(conn.local.comment.find_one({"_id": ObjectId(id_comm)}))


@router.delete('/post/comments/{id_comm}', tags=["Comments"])
async def delete_comment(id_comm,post: Post):
    return serializeDict(conn.local.comment.find_one_and_delete({"_id":ObjectId(id_comm)}))