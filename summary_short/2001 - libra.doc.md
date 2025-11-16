# Short Summary

- **Background and objectives**: Libra is an economy-driven cluster scheduler designed to maximize user utility by scheduling CPU time based on user-defined budget and deadline constraints, rather than system-centric performance metrics. It integrates with the Sun Grid Engine to provide Quality of Service (QoS) computational economy for batch jobs on a homogeneous Linux cluster.

- **In scope**:
  - Support for sequential and embarrassingly parallel batch jobs.
  - Integration with Sun Grid Engine for job queuing and resource management.
  - Implementation of a bid-based proportional resource-sharing model.
  - Use of stride scheduling for proportional CPU time allocation.
  - Job acceptance/rejection based on user budget and deadline.

- **Out of scope**:
  - Job migration for resource defragmentation.
  - Real parallel jobs with inter-job dependencies.
  - User-to-user resource bargaining mechanisms.
  - Detailed pricing and payment policy implementation.
  - Graphical user interface (GUI) in initial version.

- **Roles and core use cases**:
  - As a cluster user, I want to submit jobs with budget and deadline so that my computational needs are prioritized by utility.
  - As a cluster administrator, I want to monitor node status and adjust scheduling policies so that cluster resources are efficiently managed.
  - As a cluster user, I want to check job status and cancel jobs so that I maintain control over my submitted work.

- **Success metrics**:
  - All jobs completed within 10% of their specified deadline (assuming accurate job statistics).
  - Maximum response time for job submission under 1 minute.
  - User cost never exceeds the submitted budget under any circumstances.

- **Major constraints**:
  - Limited to a 4-node Pentium-III Linux cluster for testing.
  - Requires a simulation tool for performance analysis.
  - Must use standard C and comply with GNU General Public License.
  - No modifications to the Linux kernel allowed.
  - Scheduling heuristics used instead of exhaustive search algorithms.

- **Undecided issues**:
  - Detailed pricing mechanism for user charges.
  - Development of a custom simulation tool vs. using an available one.
  - Implementation of a GUI for user and administrator interfaces.
  - Not mentioned.
  - Not mentioned.