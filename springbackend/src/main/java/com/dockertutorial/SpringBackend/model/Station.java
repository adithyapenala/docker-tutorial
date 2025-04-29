package com.DockerTutorial.SpringBackend.model;


import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name = "station")
public class Station {

    @Id
    private int id;
    private String name;
    private String region;
    private String state;


}
