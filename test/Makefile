
CXX=g++

CXXFLAGS=-Wall -g 

PBINC=/usr/lib64/include
PBLIB=/usr/lib64/libprotobuf.a

INCS=-I./ -I../src -I${PBINC}
LIBS=${PBLIB} -lpthread

%.o : %.cpp
	${CXX} -c ${CXXFLAGS} ${INCS} $< -o $@

%.o : %.cc
	${CXX} -c ${CCFLAGS} ${INCS} $< -o $@
	
CORE_OBJECTS := test.o test.pb.o ../src/pbjson.o

all: exe

exe:  ${CORE_OBJECTS}
	${CXX} -o pbjson_test ${CORE_OBJECTS} $(LIBS)
