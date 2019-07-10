-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 12, 2019 at 10:04 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `splitter`
--

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `date_posted` datetime NOT NULL,
  `content` text NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`id`, `title`, `date_posted`, `content`, `user_id`) VALUES
(9, 'Login bug (belangrijk)', '2019-06-06 11:57:08', 'Log nooit uit, als je uitlogt krijg je een rare foutmelding. Ik heb al een idee hoe ik dit moet oplossen. ', 8),
(10, 'Jackets and Outerwear', '2019-06-06 14:24:24', 'Still going strong', 9),
(11, '<p> Test <p>', '2019-06-06 14:42:52', '<h1>Test </h1> <h3> Test2 </h3>', 8);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(120) NOT NULL,
  `image_file` varchar(20) NOT NULL,
  `password` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `image_file`, `password`) VALUES
(4, 'Lesley', 'lesleywitkamp2@gmail.com', 'default.jpg', '$2b$12$GauTw6tlPl33i79CxusqxujGAEGYkb4yOcwkjvMKEryKbs27QiCQa'),
(6, 'Kings', 'Kings@gmail.com', 'default.jpg', '$2b$12$4xM/IODqX3YJc6DXF0llyeifU/I.bFE8I1HHuvCagISxkX//IVAn.'),
(7, 'Admin', 'admin@gmail.com', 'default.jpg', '$2b$12$MQvlS3TLHbG07WkmxnV/tuPuEK/v9L4AHz.HOthuvdFrELxIE7T2.'),
(8, 'Timdeplatvis111', 'timdeplatvis@gmail.com', 'default.jpg', '$2b$12$ATu5BIMzJwFRdRM113Iireg8hYvD8Rfgpa9/rH7e.4ryrOmXOVXy6'),
(9, 'AndreKortekaas', 'andre@kingsofindigo.com', 'default.jpg', '$2b$12$7WcAwId5EmG9JtAoHjDsQ.wLyMR9D./y7v4UJsWvgbek5t7aoPpiq'),
(10, 'Testtt@gmail.com', 'Testst@gmail.com', 'default.jpg', '$2b$12$HoWjjdb3S4.ODv8gfMxvOOZINITvU2ADPIu6NxS6kVcQ82blvgcmy'),
(11, 'Yeeticusss', 'lol@gmail.com', 'default.jpg', '$2b$12$A1/rY5L7JQwEf1XULxDTBO1HzPYbVcKHWPjijlsbHsGXlyKymCZ.G'),
(12, 'Wtfisgoingon', 'Wtfisgoingon@gmail.com', 'default.jpg', '$2b$12$9i0BbOZUhqT22Um4UcyafuUdNiCBf/1sRLVyiUs87lp0Bq6YYVFLu'),
(13, 'Fuck', 'Fuck@gmail.com', 'default.jpg', '$2b$12$WmBx6kW9gmz5PCYdkPsfCOObE3TZNXnJr0XlgjSENnC8daoiU8fui'),
(14, 'FuckFascists', 'FuckFascists@gmail.com', 'default.jpg', '$2b$12$MVwi5hXgST0Qk5PgPbpS5.eVvBryTjSldqj.FWNAnx9x1PVNcO31W'),
(15, 'FINALTEST', 'FINALTEST@gmail.com', 'default.jpg', '$2b$12$OIS7rZypvvlYCvDxOUgC3u1wgq3ryEcTFAiZiuCUOpYl.raGnJW9e'),
(16, 'Iloveapplejuice', 'Iloveapplejuice@gmail.com', 'default.jpg', '$2b$12$bzGfQBfsJCBXuDvqSiXykedLgPBu4yY8Zd7yB.05GkoeScusEZFFa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `post`
--
ALTER TABLE `post`
  ADD CONSTRAINT `post_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
