import { Router } from 'express';
import { UserController } from '../Controllers/auth.js';
import { check, body } from 'express-validator';
const router = Router();
router.get('/', (req, res) => {
  console.log(req.headers);

  res.send('Hello world');
  //res.setHeader({'csrfToken' , req.csrfToken()})
});
router.post(
  '/register',
  check('email', 'Invalid email').trim().isEmail(),
  UserController.postRegister
);

export default router;
