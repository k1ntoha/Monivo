import { INTEGER, STRING, BOOLEAN } from 'sequelize';

import sequelize from '../util/database.js';

export const User = sequelize.define('Users', {
  id: {
    type: INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },
  name: { type: STRING },
  email: { type: STRING, unique: true },
  password: { type: STRING, allowNull: false },
  isActivated: { type: BOOLEAN, defaultValue: false },
  activationLink: { type: STRING, allowNull: true },
});
