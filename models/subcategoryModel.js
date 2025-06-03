import sequelize from '../util/database.js';
import { DataTypes } from 'sequelize';

const Subcategory = sequelize.define('Subcategories', {
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },
  name: {
    type: DataTypes.STRING,
    unique: true,
  },
  main_category: {
    type: DataTypes.ENUM,
    values: [
      'necessities',
      'wants',
      'savings_investments',
      'unexpected',
      'debts',
    ],
    allowNull: false,
  },
});

export { Subcategory };
