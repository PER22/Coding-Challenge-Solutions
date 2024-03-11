import React from 'react';
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import { Checkbox, FormControlLabel, Typography } from '@mui/material';
import './SolutionFilterControls.css'
const languages = ["Java", "Python", "C++"];
const difficulties = ["Easy", "Medium", "Hard"];



const SolutionFilterControls = ({ filters, setFilters, companies }) => {
    const clearFilters = () => {
        setFilters({
            language: null,
            companies: [],
            difficulty: null,
        });
    };

    const handleCompanyChange = (event) => {
        const companyName = event.target.name;
        const isChecked = event.target.checked;
        setFilters((prevFilters) => {
            const updatedCompanies = isChecked
                ? [...prevFilters.companies, companyName]
                : prevFilters.companies.filter(company => company !== companyName);

            return { ...prevFilters, companies: updatedCompanies };
        });
    };


    const handleLanguageSelect = (language) => {
        setFilters(prevFilters => ({
            ...prevFilters,
            language: prevFilters.language === language ? null : language,
        }));
    };

    const handleDifficultySelect = (difficulty) => {
        setFilters(prevFilters => ({
            ...prevFilters,
            difficulty: prevFilters.difficulty === difficulty ? null : difficulty,
        }));
    };

    return (<div id="solution-filter-controls">
        <button onClick={clearFilters}>Clear Filters</button>
        <div>
            <label>
                Language:
                <ButtonGroup >
                    {languages.map(lang => (
                        <Button
                            key={lang}
                            onClick={() => handleLanguageSelect(lang)}
                            sx={{
                                color: 'black',
                                '@media (prefers-color-scheme: dark)': {
                                    color: 'white',
                                }
                            }}
                        >
                            {lang}
                        </Button>
                    ))}
                </ButtonGroup >

            </label>
        </div>
        <div>
            <label>
                <Typography>Difficulty</Typography>
                <ButtonGroup sx={{
                    '.MuiButton-root': { // Target all Button components within the ButtonGroup
                        border: 0, // Remove border
                        outline: 0, // Remove outline
                        '&:hover': {
                            border: 0, // Remove border on hover
                        },
                        '&:focus': {
                            outline: 0, // Remove focus outline
                        },

                    },
                }}
                >
                    {difficulties.map(diff => (
                        <Button
                            key={diff}
                            onClick={() => handleDifficultySelect(diff)}
                            sx={{
                                color: 'black',
                                backgroundColor: filters.difficulty === diff
                                    ? (diff === 'Easy' ? '#2f9e44' : diff === 'Medium' ? '#fab005' : '#f03e3e')
                                    : (diff === 'Easy' ? '#b2f2bb' : diff === 'Medium' ? '#ffec99' : '#ff7979'),
                                '&:hover': {
                                    backgroundColor: filters.difficulty === diff
                                        ? (diff === 'Easy' ? '#278a36' : diff === 'Medium' ? '#e69900' : '#d63333') // Slightly darker vibrant colors for hover
                                        : (diff === 'Easy' ? '#a3e9a4' : diff === 'Medium' ? '#ffe066' : '#ffb2b2'), // Slightly darker pastel colors for hover
                                },

                                border: 0, // Remove border

                            }}
                        >
                            {diff}
                        </Button>
                    ))}
                </ButtonGroup>
            </label>
        </div>
        <Typography>Companies:</Typography>
        <div id='companies-section'>
            {companies.map((company, index) => (
                <div className='each-company'>
                    <FormControlLabel
                        key={index}
                        control={
                            <Checkbox
                                checked={filters.companies.includes(company.name)}
                                onChange={handleCompanyChange}
                                name={company.name}
                                sx={{
                                    '@media (prefers-color-scheme: dark)': {
                                        color: 'white',
                                    },

                                    paddingTop: 0,
                                    paddingBottom: 0,
                                }}
                            />
                        }
                        label={company.name}
                    />
                </div>
            ))}
        </div>


    </div>);
};

export default SolutionFilterControls
