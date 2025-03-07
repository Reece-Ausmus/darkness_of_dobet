import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import MenuBar from "./Components/MenuBar";

const App: React.FC = () => {
  return (
    <Router>
      <MenuBar />
    </Router>
  );
};

export default App;
