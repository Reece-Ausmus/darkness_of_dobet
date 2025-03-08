//import axios from "axios";
import React from "react";

type MapType = number[][][];

type MapProps = {
  map: MapType;
};

/*
const fetchMap = async (): Promise<void> => {
  try {
    const response = await axios.get("http://127.0.0.1:5000/get_map");
    setMap(response.data.map);
  } catch (error) {
    console.error("Error fetching map:", error);
  }
};
*/

const Map: React.FC<MapProps> = ({ map }) => {
  return (
    <div>
      <h1>Map</h1>
      <pre>{JSON.stringify(map, null, 2)}</pre>
    </div>
  );
};

export default Map;
