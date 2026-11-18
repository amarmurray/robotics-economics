# Instructor solutions — shadow data and customer qualification

Keep this separate from the student packet.

1. Couple identical B initial state and exogenous inputs. Require every B transition/output parent (controller, order demand, pricing, dispatch, operator recovery, resources, rights and capture overhead) to remain unchanged under copying. Induct over time. Pinned weights do not rule out additional operator-delay changes: one of B's whole orders can fail under the same controller.
2. Let Π(D) be the attainable policy set with D. Under free optional data and unchanged feasibility, Π(D)⊆Π(D∪{d}), so max_Π V cannot fall. If a forced update costing 1/4 produces no qualifying new service, incremental net is −1/4; a retained no-training option yields zero.
3. Supported contribution (3/5)(1/2)=3/10. Unsupported contribution ranges from zero to (2/5)2=4/5, so gross in [3/10,11/10], net in [1/20,17/20]. Net shadow = 1/20+(2/5)x; specialist net=2/5; shadow strictly wins when x>7/8. The data given do not establish that inequality.
4. Fréchet bounds: q∈[max(0,1/2+3/4−1),min(1/2,3/4)]=[1/4,1/2]. With 2 periods and cost 1/4, net=2q−1/4∈[1/4,3/4]. Independence imposes q=3/8 and net=1/2. The four joint cells are q,1/2−q,3/4−q,q−1/4.
5. No service dates remain, so forced paid learning returns −1/4; an ex-ante operator choosing F instead earns incremental zero. An offline capability score is not a sale once customer demand expires.
6. F may never take the target embodiment's recovery-critical action. Two worlds can match F logs and all source-only scores while delivering respectively zero and 2 units after that action. Identification requires safely approved target-action whole-service observations, valid structural transfer/transport evidence or interval bounds; hard simultaneous operator capacity must be certified separately. All values are hypothetical, not empirical robotics estimates.
