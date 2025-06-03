class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }
}

const createUserDto = (usr) => {
  return new User(usr.name, usr.email);
};

export { createUserDto };
