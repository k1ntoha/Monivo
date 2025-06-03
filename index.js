import express from 'express';
import jsonParser from 'body-parser';
import sequelize from './util/database.js';
import dotenv from 'dotenv';
import cors from 'cors';
import router from './router/router.js';
import { User } from './models/userModel.js';
import { Session } from './models/sessionModel.js';
import { Transaction } from './models/transactionModel.js';
import { Subcategory } from './models/subcategoryModel.js';
import { TransactionCategory } from './models/transactionCategoryModel.js';

dotenv.config();

const PORT = process.env.PORT || 3000;

const app = express();

app.use(jsonParser.urlencoded({ extended: false }));

app.use(
  cors({
    origin: 'http://localhost:3000',
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    credentials: true,
  })
);

app.use('/', router);

//Error
app.use((error, req, res, next) => {
  if (error) {
    res.redirect('/error-occurred');
  }
});

// Associations
User.hasMany(Session, {
  foreignKey: 'userId',
  onDelete: 'CASCADE',
  hooks: true,
});
Session.belongsTo(User, {
  foreignKey: 'userId',
  onDelete: 'CASCADE',
  hooks: true,
});

User.hasMany(Transaction, {
  foreignKey: 'userId',
  onDelete: 'CASCADE',
  hooks: true,
});
Transaction.belongsTo(User, {
  foreignKey: 'userId',
  onDelete: 'CASCADE',
  hooks: true,
});

Transaction.belongsToMany(Subcategory, {
  through: TransactionCategory,
  foreignKey: 'transaction_id',
  otherKey: 'subcategory_id',
  onDelete: 'CASCADE',
  hooks: true,
});
Subcategory.belongsToMany(Transaction, {
  through: TransactionCategory,
  foreignKey: 'subcategory_id',
  otherKey: 'transaction_id',
  onDelete: 'CASCADE',
  hooks: true,
});

async function start() {
  await sequelize
    .sync({ alter: true })
    .then((result) => {
      app.listen(PORT, () => {
        console.log('SERVER is ON ...');
      });
    })
    .catch((err) => {
      console.log(err);
    });
}
start();
