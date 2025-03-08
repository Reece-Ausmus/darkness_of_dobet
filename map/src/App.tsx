import React, { useState } from "react";
import { BrowserRouter as Router } from "react-router-dom";
import MenuBar from "./Components/MenuBar";
import Map from "./Components/Map";

type MapType = number[][][];

const App: React.FC = () => {
  const [map, setMap] = useState<MapType>([]);

  return (
    <Router>
      <MenuBar setMap={setMap} />
      <Map map={map} />
    </Router>
  );
};

export default App;
