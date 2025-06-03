import { User } from '../models/userModel.js';
import bcrypt from 'bcrypt';
import { createUserDto } from '../util/userDto.js';
import { validationResult } from 'express-validator';

let postLogin = async (req, res, next) => {
  const { email, password } = req.body;
  let user = await User.findOne({ email: email });
  if (!user) {
    return res.redirect('/login');
  }
  if (bcrypt.compareSync(password, user.password)) {
    req.session.isLoggedIn = true;
    req.session.user = createUserDto(user);
    return req.session.save((err) => {
      console.log(err);
      return res.redirect('/');
    });
  }
  res.redirect('/login');
};

let postLogOut = (req, res, next) => {
  req.session.destroy((err) => {
    console.log(err);
    res.redirect('/');
  });
  return next();
};

let postRegister = async (req, res, next) => {
  const { email, password, name } = req.body;
  const errors = validationResult(req);
  if (errors) {
    return res.status(422);
  }
};

export const UserController = {
  postLogin,
  postLogOut,
  postRegister,
};
