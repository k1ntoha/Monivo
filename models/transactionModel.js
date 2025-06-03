import sequelize from '../util/database.js';
import { DataTypes } from 'sequelize';

const Transaction = sequelize.define('Transactions', {
  id: {
    type: sequelize.Sequelize.INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },
  userId: {
    type: sequelize.Sequelize.INTEGER,
    allowNull: false,
  },
  merchant: DataTypes.STRING,
  amount: DataTypes.BIGINT,
  currency: {
    type: DataTypes.STRING,
    defaultValue: 'UZS',
  },
  transaction_type: DataTypes.STRING,
  description: DataTypes.TEXT,
  original_source: DataTypes.STRING,
  raw_input: DataTypes.TEXT,
  created_at: {
    type: DataTypes.DATE,
    defaultValue: DataTypes.NOW,
  },
});
export { Transaction };
