import React, { useState, useEffect } from "react";
import { BrowserRouter as Router } from "react-router-dom";
import MenuBar from "./Components/MenuBar";
import axios from 'axios';

type Map = number[][][];

const App: React.FC = () => {
  const [map, setMap] = useState<Map>([]);

  const fetchMap = async (): Promise<void> => {
    try {
        const response = await axios.get("http://127.0.0.1:5000/get_map");
        setMap(response.data.map);
    } catch (error) {
        console.error("Error fetching map:", error);
    }
  };

  return (
    <Router>
      <MenuBar />
      <div>
        <button onClick={fetchMap}>fetchMap</button>
        {map} HAHA MAP
      </div>
    </Router>
  );
};

export default App;
