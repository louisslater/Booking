SET @date_param := '2024-05-02';
SET @booking_datetime_1 := CONCAT(@date_param, ' 10:00:00');
SET @booking_datetime_2 := CONCAT(@date_param, ' 11:00:00');
SET @booking_datetime_3 := CONCAT(@date_param, ' 12:00:00');
SET @booking_datetime_4 := CONCAT(@date_param, ' 13:00:00');

-- Insert queries using prepared statements
PREPARE stmt FROM '
    INSERT INTO bookings (name, email, booking_datetime, booked)
    VALUES (null, null, ?, 0)
';
EXECUTE stmt USING @booking_datetime_1;
EXECUTE stmt USING @booking_datetime_2;
EXECUTE stmt USING @booking_datetime_3;
EXECUTE stmt USING @booking_datetime_4;
DEALLOCATE PREPARE stmt;

