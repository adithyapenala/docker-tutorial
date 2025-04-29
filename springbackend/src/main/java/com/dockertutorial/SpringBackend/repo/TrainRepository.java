package com.DockerTutorial.SpringBackend.repo;

import com.DockerTutorial.SpringBackend.model.Train;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.Date;
import java.util.List;
import java.util.Optional;

public interface TrainRepository extends JpaRepository<Train, Integer> {

      @Query(value = "SELECT t FROM Train t where t.from_station = :from_station and t.to_station = :to_station")
      List<Train> findTrainsByFrom_stationAndTo_station(@Param("from_station") int from_station, @Param("to_station") int to_station);

      @Query(value = "SELECT t FROM Train t where t.from_station = :from_station")
      List<Train> findTrainsByFrom_station(@Param("from_station") int station);

      @Query(value = "SELECT t FROM Train t where t.to_station = :to_station")
      List<Train> findTrainsByTo_station(@Param("to_station") int station);

      @Query("SELECT t FROM Train t WHERE t.from_station = :from_station AND t.to_station = :to_station AND t.start_date = :start_date")
      List<Train> findByFrom_stationAndTo_stationAndStart_date(@Param("from_station") int from_station,
                                                               @Param("to_station") int to_station,
                                                               @Param("start_date") Date start_date);
}