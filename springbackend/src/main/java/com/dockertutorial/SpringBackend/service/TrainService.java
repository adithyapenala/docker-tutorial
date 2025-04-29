package com.DockerTutorial.SpringBackend.service;

import com.DockerTutorial.SpringBackend.model.Station;
import com.DockerTutorial.SpringBackend.model.Train;
import com.DockerTutorial.SpringBackend.repo.StationRepository;
import com.DockerTutorial.SpringBackend.repo.TrainRepository;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Optional;

@Service
public class TrainService {
    private final TrainRepository trainRepository;

    public TrainService(TrainRepository trainRepository) {
        this.trainRepository = trainRepository;
    }

    public List<Train> getAllTrains() {
        return trainRepository.findAll();
    }

    public Train searchTrainById(int id) {
        return trainRepository.findById(id).orElse(new Train());
    }

    public List<Train> searchTrainByStation(int fromStation, int toStation) {
        return trainRepository.findTrainsByFrom_stationAndTo_station(fromStation, toStation);
    }

    public List<Train> searchFromTrainByStation(int Station) {

        return trainRepository.findTrainsByFrom_station(Station);
    }

    public List<Train> searchToTrainByStation(int Station) {

        return trainRepository.findTrainsByTo_station(Station);
    }

    public List<Train> searchTrainsByFromToDate(int from, int to, Date date) {
        return trainRepository.findByFrom_stationAndTo_stationAndStart_date(from, to, date);
    }

}
