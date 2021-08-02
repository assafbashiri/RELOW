from server.DB.DAO.UsersDAO import UsersDAO
from server.DB.DTO.UserDTO import UserDTO


class UsersMapper:

    def __init__(self, conn):
        self.dao = UsersDAO(conn)
      #  self.UsersMapper = singleton

    def addUser(self, user):
        userDTO = UserDTO(user.user_id,user.first_name,user.last_name,user.email,user.password)
        self.dao.insert(userDTO)
        self.UsersMapper.put(user)
    def removeUser(self,user):
        self.dao.delete(user.user_id)
        self.UsersMapper.remove(user.user_id)
    def updateFirstname(self, user, firstname):
        self.dao.updateFirstname(user.user_id, firstname)
        self.UsersMapper.get(user.user_id).first_name = firstname

    def updateLastname(self, user, lastname):
        self.dao.updateLastname(user.user_id, lastname)
        self.UsersMapper.get(user.user_id).last_name = lastname

    def updateUsername(self, user, username):
        self.dao.updateUsername(user.user_id, username)
        self.UsersMapper.get(user.user_id).user_name = username

    def updatePassword(self, user, password):
        self.dao.updatePassword(user.user_id, password)
        self.UsersMapper.get(user.user_id).password = password







