import React, { useState } from 'react';

const languages = ["Java", "Python", "C++"];
const difficulties = ["Easy", "Medium", "Hard"];

const SolutionFilterControls = ({ filters, setFilters }) => {
    const [companyInput, setCompanyInput] = useState('');

    const clearFilters = () => {
        setFilters({
            language: null,
            companies: [],
            difficulty: null,
        });
    };

    const addCompany = () => {
        if (companyInput && !filters.companies.includes(companyInput)) {
            setFilters(prevFilters => ({
                ...prevFilters,
                companies: [...prevFilters.companies, companyInput],
            }));
            setCompanyInput('');
        }
    };

    const removeCompany = (company) => {
        setFilters(prevFilters => ({
            ...prevFilters,
            companies: prevFilters.companies.filter(c => c !== company),
        }));
    };

    const handleLanguageChange = (event) => {
        setFilters(prevFilters => ({
            ...prevFilters,
            language: event.target.value,
        }));
    };

    const handleDifficultyChange = (event) => {
        setFilters(prevFilters => ({
            ...prevFilters,
            difficulty: event.target.value,
        }));
    };

    return (
        <div>
            <button onClick={clearFilters}>Clear Filters</button>
            <div>
                <label>
                    Language:
                    <select value={filters.language || ''} onChange={handleLanguageChange}>
                        <option value="">Select Language</option>
                        {languages.map(lang => (
                            <option key={lang} value={lang}>{lang}</option>
                        ))}
                    </select>
                </label>
            </div>
            <div>
                <label>
                    Difficulty:
                    <select value={filters.difficulty || ''} onChange={handleDifficultyChange}>
                        <option value="">Select Difficulty</option>
                        {difficulties.map(diff => (
                            <option key={diff} value={diff}>{diff}</option>
                        ))}
                    </select>
                </label>
            </div>
            <div>
                <label>
                    Add Company:
                    <input
                        type="text"
                        value={companyInput}
                        onChange={(e) => setCompanyInput(e.target.value)}
                    />
                </label>
                <button onClick={addCompany}>Add</button>
            </div>
            {filters.companies.length > 0 && (
                <div>
                    <h4>Companies:</h4>
                    <ul>
                        {filters.companies.map((company, index) => (
                            <li key={index}>{company} <button onClick={() => removeCompany(company)}>Remove</button></li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default SolutionFilterControls;
