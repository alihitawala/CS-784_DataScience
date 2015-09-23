CREATE TABLE `test`.`Quickr` (
  `id` INT NOT NULL COMMENT '',
  `color` VARCHAR(45) NOT NULL COMMENT '',
  `starting_system` VARCHAR(45) NOT NULL COMMENT '',
  `bike_name` VARCHAR(45) NOT NULL COMMENT '',
  `price` INT NOT NULL COMMENT '',
  `company` VARCHAR(45) NOT NULL COMMENT '',
  `owner` VARCHAR(45) NOT NULL COMMENT '',
  `city_posted` VARCHAR(45) NOT NULL COMMENT '',
  `model_year` INT NOT NULL COMMENT '',
  `new_bike_price` INT NOT NULL COMMENT '',
  `fuel_type` VARCHAR(45) NOT NULL COMMENT '',
  `km_driven` INT NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '');

ALTER TABLE `test`.`Quickr`
CHANGE COLUMN `id` `BikeId` INT(11) NOT NULL COMMENT '' ,
CHANGE COLUMN `color` `Color` VARCHAR(45) NOT NULL COMMENT '' ,
CHANGE COLUMN `starting_system` `StartingSystem` VARCHAR(45) NOT NULL COMMENT '' ,
CHANGE COLUMN `bike_name` `BikeName` VARCHAR(45) NOT NULL COMMENT '' ,
CHANGE COLUMN `price` `Price` INT(11) NOT NULL COMMENT '' ,
CHANGE COLUMN `company` `BikeCompany` VARCHAR(45) NOT NULL COMMENT '' ,
CHANGE COLUMN `owner` `Owner` VARCHAR(45) NOT NULL COMMENT '' ,
CHANGE COLUMN `city_posted` `CityPosted` VARCHAR(45) NOT NULL COMMENT '' ,
CHANGE COLUMN `model_year` `ModelYear` INT(11) NOT NULL COMMENT '' ,
CHANGE COLUMN `new_bike_price` `NewBikePrice` INT(11) NOT NULL COMMENT '' ,
CHANGE COLUMN `fuel_type` `FuelType` VARCHAR(45) NOT NULL COMMENT '' ,
CHANGE COLUMN `km_driven` `KmDriven` INT(11) NOT NULL COMMENT '' ;
