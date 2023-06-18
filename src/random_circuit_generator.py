import cirq

#This is a method to generate random circuits that will be import through Jabalizer to generate a circuit in ICM format.
# For the sake of simplicity, we will limit the types of gate to 3 gates: H, T and CNOT.
# In the function, the parameters require:
#    + numqubits(number of qubits): to identify a circuit of how many qubits it should create.
#    + moments (moments): This is a concept related to Cirq. For more information on moments, here's a link: https://quantumai.google/cirq/build/circuits
# After generating a random circuit, the function will store it in a seperate file in JSON format.


def randomcirq(numqubits,moments):

    line_qubits = []

    for i in range(numqubits):
        line_qubits.append(cirq.LineQubit(i))

    circuit = cirq.testing.random_circuit(line_qubits,moments,1.0,{cirq.H : 1, cirq.T: 1, cirq.CNOT: 2})

    print(circuit)

    f = open("random_circuit", "w")

    f.write(cirq.to_json(circuit))

    f.close
