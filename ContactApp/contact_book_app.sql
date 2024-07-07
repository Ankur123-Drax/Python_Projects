-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 29, 2023 at 03:42 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `contact_book_app`
--

-- --------------------------------------------------------

--
-- Table structure for table `contactlist`
--

CREATE TABLE `contactlist` (
  `name` char(100) NOT NULL,
  `phone1` bigint(12) NOT NULL,
  `email` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone2` bigint(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contactlist`
--

INSERT INTO `contactlist` (`name`, `phone1`, `email`, `address`, `phone2`) VALUES
('Ankur2', 2134567891, 'ankur111@gmail.com', 'vishnapuri', NULL),
('Ankur123', 7071832015, 'a@gmail.com', 'hhhhhhhh', 7418529630),
('Ankur1', 7415263898, 'ankur12345@gmail.com', 'bamrauli', 2637485960);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contactlist`
--
ALTER TABLE `contactlist`
  ADD PRIMARY KEY (`phone1`,`email`),
  ADD UNIQUE KEY `phone1` (`phone1`),
  ADD UNIQUE KEY `email` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
