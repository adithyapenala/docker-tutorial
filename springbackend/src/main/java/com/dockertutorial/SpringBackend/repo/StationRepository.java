package com.DockerTutorial.SpringBackend.repo;

import com.DockerTutorial.SpringBackend.model.Station;
import org.springframework.data.jpa.repository.JpaRepository;

public interface StationRepository extends JpaRepository<Station, Integer> {
    Station findStationById(int id);

    Station findStationByName(String fromStation);
}
