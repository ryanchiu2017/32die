import cirq

circuit = cirq.Circuit()
(q0, q1, q2, q3, q4) = cirq.LineQubit.range(5)

circuit.append([cirq.H(q0), cirq.H(q1), cirq.H(q2), cirq.H(q3), cirq.H(q4)])
circuit.append([cirq.X(q1)])
circuit.append([cirq.measure(q0, q1, q2, q3, q4, key='result')])
sim = cirq.Simulator()
results=sim.run(circuit)
print(results)
print(results.histogram(key='result'))
