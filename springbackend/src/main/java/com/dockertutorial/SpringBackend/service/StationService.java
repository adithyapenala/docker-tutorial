package com.DockerTutorial.SpringBackend.service;

import com.DockerTutorial.SpringBackend.model.Station;
import com.DockerTutorial.SpringBackend.repo.StationRepository;

public class StationService {
    public final StationRepository stationRepository;
    public StationService(StationRepository stationRepository) {
        this.stationRepository = stationRepository;
    }

    public Station getStationById(int id) {
        return stationRepository.findStationById(id);
    }
}
