import sequelize from '../util/database.js';
import { DataTypes } from 'sequelize';

const Session = sequelize.define('Sessions', {
  id: {
    type: sequelize.Sequelize.INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },

  userId: {
    type: sequelize.Sequelize.INTEGER,
    allowNull: false,
  },

  refreshToken: {
    type: sequelize.Sequelize.STRING,
    allowNull: false,
  },

  user_agent: DataTypes.STRING,
  ip_address: DataTypes.STRING,
  created_at: {
    type: DataTypes.DATE,
    defaultValue: DataTypes.NOW,
  },
});

export { Session };
