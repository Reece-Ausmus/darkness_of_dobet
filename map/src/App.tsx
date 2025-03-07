import React, { useState } from "react";
import "./App.css";

const BOARD_SIZE = 8;

const initialBoard = () => {
  const board = Array(BOARD_SIZE)
    .fill(null)
    .map(() => Array(BOARD_SIZE).fill(null));
  // Place the king at E1 (4, 7) for white
  board[7][4] = "K";
  return board;
};

const ChessBoard: React.FC = () => {
  const [board, setBoard] = useState(initialBoard());

  return (
    <div className="chessboard">
      {board.map((row, rowIndex) => (
        <div key={rowIndex} className="row">
          {row.map((cell, colIndex) => (
            <div
              key={colIndex}
              className={`cell ${
                (rowIndex + colIndex) % 2 === 0 ? "light" : "dark"
              }`}
            >
              {cell === "K" && <span className="piece">♔</span>}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

const App: React.FC = () => {
  return (
    <div className="App">
      <h1>Chess Simulator</h1>
      <ChessBoard />
    </div>
  );
};

export default App;
