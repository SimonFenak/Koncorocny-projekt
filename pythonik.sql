-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hostiteľ: 127.0.0.1
-- Čas generovania: St 07.Jún 2023, 11:34
-- Verzia serveru: 10.4.24-MariaDB
-- Verzia PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databáza: `pythonik`
--

-- --------------------------------------------------------

--
-- Štruktúra tabuľky pre tabuľku `main`
--

CREATE TABLE `main` (
  `meno` varchar(20) NOT NULL,
  `heslo` varchar(20) NOT NULL,
  `raketka` int(10) NOT NULL,
  `fareb` int(11) NOT NULL,
  `bludisko` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Sťahujem dáta pre tabuľku `main`
--

INSERT INTO `main` (`meno`, `heslo`, `raketka`, `fareb`, `bludisko`) VALUES
('jakub', 'petrila', 14, 26, 0),
('feko', '123', 10, 0, 16.8613);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
