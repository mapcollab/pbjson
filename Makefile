#!/bin/make

#
# Copyright (C) 2015-2017 Thales Avionics, Inc.
#

SRC_DIR:=./src
INC_DIR:=./src

TARGET:=libpbjson.so

SRCS := $(wildcard $(SRC_DIR)/*.cpp)
OBJS := $(SRCS:.cc=.o) $(SRCS:.cpp=.o)

LIBS:=-lpthread -lprotobuf
CXX:=g++
override CXXFLAGS ?= -O2
override CXXFLAGS += -shared -FPIC -fPIC -g -I$(INC_DIR) -Wall -Werror

all: build

build:
	$(CXX) -c $(CXXFLAGS) -o $(TARGET) $(SRCS) $(LIBS)

.PHONY: clean all build

clean:
	@rm -f $(TARGET)
