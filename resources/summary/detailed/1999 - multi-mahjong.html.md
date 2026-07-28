# Detailed Summary: MultiMahjong Project

## Background and Scope
MultiMahjong is a client-server computer game enabling single-player (standalone) or multiplayer (networked) Mahjong. The system comprises a MultiMahjongServer for managing network games and a MultiMahjongClient for user interaction. The core scope includes supporting up to four players (humans and computer opponents) following Chinese Mahjong rules, with essential networking via TCP/IP. Non-goals include advanced security (no encryption), multi-language support (Level 3), and server-side computer opponents (Level 3).

## Stakeholders Matrix and Use Cases
- **Steve Goschnick (Client)** – Managing Director of Solid Software Pty Ltd; provides commercial requirements and final acceptance.
- **K-Team (Development Team)** – Implements and delivers the MultiMahjong product per SRS.
- **End Users (Players)** – Play Mahjong via the client; require intuitive GUI and adherence to rules.
- **Server Administrator** – Operates the MultiMahjongServer; needs setup and troubleshooting documentation.
- **Computer Opponent (CO)** – Automated player following Mahjong rules; processes moves within constraints.

**Main Scenarios:**  
1. User starts client, chooses new single/multiplayer game or joins existing game.  
2. User configures game (name, icon, score limit, opponent mix).  
3. Server initializes game (tile randomization, seating) and relays data.  
4. Players take turns picking/discarding tiles; client validates moves per Chinese rules.  
5. Client notifies eligible actions (Chow/Pung/Kong/Mahjong) and updates display.  
6. Game ends after four rounds or early exit; clients return to main menu.  
7. CO calculates moves without accessing hidden tile data.  
8. Error handling displays dialogue boxes for fatal/nonfatal issues.

**Exception Scenarios:**  
- Player disconnects mid-game; CO replaces them (Level 2).  
- Network failure; client handles disconnection gracefully.

## Business Process
**Main Process: Play Multiplayer Game**  
1. **Trigger:** User selects "create new multi player game."  
2. **Input:** User provides name, icon, opponent count, score limit.  
3. Client sends initialization data to server.  
4. Server sets up game, randomizes tiles/seating, notifies clients.  
5. **Loop:** Players take turns—pick tile, discard, or claim discard for sets.  
6. Client validates moves against Chinese rules, updates GUI.  
7. **Output:** Game ends after four rounds; scores displayed.  
8. Clients return to main menu.

**Key Branch: Single-Player Game**  
1. User selects "new single player game."  
2. Input name, icon, score limit.  
3. Client internally manages three COs (no server).  
4. Play proceeds as main process but locally.

**Key Branch: Join Existing Game**  
1. User selects "join existing game."  
2. Client fetches available games list from server.  
3. User picks game, provides name/icon.  
4. Client joins; server relays game data.

## Domain Model
- **Player** – name (required), icon, score, wind position, isHuman (boolean).  
- **Game** – gameID (unique), scoreLimit (required), currentRound, windOfRound (reference to Player).  
- **Tile** – tileID (unique), suit, value, position (The Wall/Discard/Dead Tile/Exposed Set/Revealed Kong).  
- **Hand** – player (reference), tiles (list of Tile).  
- **Move** – type (Pick/Discard/Chow/Pung/Kong/Mahjong), tile (reference), player (reference).  
- **ComputerOpponent** – abilityLevel, player (reference).  
- **ServerSession** – sessionID (unique), connectedClients (list), game (reference).  
- **Preferences** – soundOn (boolean), limitForWinningHand.

## Interfaces and Integrations
- **MultiMahjongClient to MultiMahjongServer** – Direction: Bidirectional; Interaction: TCP/IP socket communication; Input: Player actions, join requests; Output: Game state updates, tile data; SLA: CO response <1 min, move calculation <5 sec.
- **MultiMahjongClient GUI** – System: Client; Direction: User to system; Interaction: Mouse/keyboard input; Input: Clicks, keystrokes; Output: Screen updates, sound effects; SLA: Updates within 1 sec of server data.
- **MultiMahjongServer to MultiMahjongClient (Broadcast)** – Direction: Server to clients; Interaction: Game state relay; Input: Move validations; Output: Player actions, score changes; SLA: Handle up to 10 simultaneous games (40 players).

## Acceptance Criteria
- **Given** a user starts the client, **when** they choose a new single-player game and enter details, **then** the game begins with three COs and follows Chinese rules.
- **Given** a multiplayer game with four human players, **when** a player discards a tile, **then** other clients are notified and can claim it if rules allow.
- **Given** a CO is active, **when** it is its turn, **then** it responds within 1 minute without accessing hidden tiles.
- **Given** a network error occurs, **when** it is nonfatal, **then** a dialogue box appears and game continues.

## Non-Functional Metrics
- **Performance:** CO response ≤1 minute; client calculates possible moves ≤5 seconds.
- **Reliability:** Server supports 10 simultaneous games; client handles disconnections gracefully.
- **Security:** No encryption; data not private.
- **Compliance:** Follows Chinese Mahjong rules; uses JDK 1.2 and Sun coding standards.
- **Observability:** Server logs available (Level 2); error dialogue boxes provide troubleshooting.

## Milestones and Release Strategy
1. Finalize SRS and client sign-off.
2. Complete architectural design (SADD) and core domain model.
3. Implement server-client communication and basic GUI.
4. Integrate Chinese rules engine and CO logic.
5. Testing against Level 1 requirements.
6. Delivery with documentation (user/admin manuals).

## Risk List and Mitigation Strategies
1. **Network latency affects gameplay** – Mitigation: Optimize data packets; set timeouts.
2. **CO algorithm too slow** – Mitigation: Limit look-ahead; use heuristic fallbacks.
3. **Cross-platform issues (JDK 1.2)** – Mitigation: Test on Windows, Mac, Unix early.
4. **Rule complexity leads to bugs** – Mitigation: Unit test all rule permutations.
5. **Insufficient server capacity** – Mitigation: Design for scalability; monitor performance.
6. **GUI not intuitive for novices** – Mitigation: User testing with varied skill levels.
7. **Documentation incomplete** – Mitigation: Assign dedicated writer; review cycles.
8. **Scope creep from Level 2/3 features** – Mitigation: Prioritize Level 1; defer extras.

## Undecided Issues and Responsible Parties
1. **Graphical details of GUI** – To be finalized in SDD; responsible: K-Team.
2. **Tile class structure** – To be decided in SDD; responsible: K-Team.
3. **High Scores list implementation** – Level 2 feature; feasibility TBD; responsible: K-Team.
4. **Sound effect formats** – Level 2; specifics pending; responsible: K-Team.
5. **Animation techniques** – Level 3; dependent on time; responsible: K-Team.
6. **Multi-language support** – Level 3; Unicode handling TBD; responsible: K-Team.
7. **Chat functionality** – Level 3; design deferred; responsible: K-Team.
8. **Server GUI for admin** – Level 2; requirements to be detailed later; responsible: K-Team.