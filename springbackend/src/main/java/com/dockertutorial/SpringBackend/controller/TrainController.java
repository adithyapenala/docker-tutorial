package com.DockerTutorial.SpringBackend.controller;

import com.DockerTutorial.SpringBackend.model.Train;
import com.DockerTutorial.SpringBackend.repo.TrainRepository;
import com.DockerTutorial.SpringBackend.service.TrainService;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.util.Date;
import java.util.List;

@Controller
public class TrainController {

    private final TrainService trainService;

    public TrainController(TrainService trainService) {
        this.trainService = trainService;
    }

    @QueryMapping
    public List<Train> allTrains() {
       return  trainService.getAllTrains();
    }

    @QueryMapping
    public Train trainById(@Argument int id) {
        return trainService.searchTrainById(id);
    }

    @QueryMapping
    public List<Train> trainsByFromTo(@Argument int from_station, @Argument int to_station) {
        return trainService.searchTrainByStation(from_station, to_station);
    }

    @QueryMapping
    public List<Train> trainsByFrom(@Argument int from_station) {
        return trainService.searchFromTrainByStation(from_station);
    }

    @QueryMapping
    public List<Train> trainsByTo(@Argument int to_station) {
        return trainService.searchToTrainByStation(to_station);
    }

    @QueryMapping
    public List<Train> trainsByFromToDate(@Argument int from_station, @Argument int to_station, @Argument String start_date) throws ParseException {

        // Creating an object of Date class with reference
        // to SimpleDateFormat class and
        // lately parsing the above string into it
        Date date = new SimpleDateFormat("yyyy-MM-dd")
                .parse(start_date);
        return trainService.searchTrainsByFromToDate(from_station, to_station, date);
    }
}
