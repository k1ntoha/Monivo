import { Sequelize } from 'sequelize';

const sequelize = new Sequelize('Monivo', 'postgres', 'admin123', {
  host: 'localhost',
  dialect: 'postgres',
});

try {
  await sequelize.authenticate();
  console.log('Connection!');
} catch (error) {
  console.log(error);
}

export default sequelize;
