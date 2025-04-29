package com.DockerTutorial.SpringBackend.model;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class User {
    private String id;
    private String name;
    private String email;

    // Constructors, getters, setters
    public User(String id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }
}