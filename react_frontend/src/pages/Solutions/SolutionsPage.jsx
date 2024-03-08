import React, { useState, useEffect } from 'react';
import { fetchSolutions } from '../../utilities/solutions-service';
import SolutionTable from './components/SolutionTable';
import SolutionFilterControls from './components/SolutionFilterControls'
import { IconButton } from '@mui/material';
import FilterListIcon from '@mui/icons-material/FilterList';
import FilterListOffIcon from '@mui/icons-material/FilterListOff';


const SolutionsPage = () => {
  const [solutions, setSolutions] = useState([]);
  const [filters, setFilters] = useState({
    language: null,
    companies: [],
    difficulty: null
  });
  const [filtersShown, setFiltersShown] = useState(true);
  const showFilters = () => {setFiltersShown(true)}
  const hideFilters = () => {setFiltersShown(false)}
  

  //Filters
  useEffect(() => {
    async function getSolutions(filters) {
      const response = await fetchSolutions(filters);
      setSolutions(response);
    }
    getSolutions(filters);
  }, [filters]);

  return (
    <div>
      <IconButton onClick={filtersShown? hideFilters : showFilters}>
        {filtersShown ?  <FilterListOffIcon sx={{color: 'white'}}/> : <FilterListIcon sx={{color: 'white'}}/>}
      </IconButton>
      {filtersShown &&
        <>
          <h1>Filters</h1>
          <SolutionFilterControls filters={filters} setFilters={setFilters} />
        </>
      }

      <h1>Solutions</h1>
      <SolutionTable solutions={solutions} ></SolutionTable>
    </div>
  );
};

export default SolutionsPage;
