SELECT   Address.city , Address.state, person.lastName, person.firstName
FROM  person
LEFT JOIN  Address
ON person.personid = address.personid;

-- UNION

-- SELECT Address.city , Address.state, person.lastName, person.firstName
-- FROM person
-- RIGHT JOIN Address
-- ON person.personid = address.personid;
