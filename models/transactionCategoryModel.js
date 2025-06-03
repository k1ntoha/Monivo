import sequelize from '../util/database.js';
import { DataTypes } from 'sequelize';

const TransactionCategory = sequelize.define('Transaction_categories', {
  transaction_id: {
    type: DataTypes.UUID,
    primaryKey: true,
  },
  subcategory_id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
  },
  assigned_by_ai: {
    type: DataTypes.BOOLEAN,
    defaultValue: false,
  },
  confidence_score: {
    type: DataTypes.FLOAT,
    defaultValue: 1.0,
  },
});

export { TransactionCategory };
