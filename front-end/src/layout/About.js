import React from 'react'

 function About() {
    return (
        <React.Fragment>
            <div class="text-body">
            <br/>
            <h1>About</h1>
            <br/>
            <p>This is a project created by Parul and Mario.
                The project aims to simulate an application tracking software.
            </p>
            <br/>
            <h2> For Recruiters</h2>
            <p>Recruiters can post jobs and specify which skills they are looking for.
                 When applicants upload their resumes, our software will determine if
                 a candidate has the skills. Recruiter can then select who to proceed with
                 based on our rating.
            </p>
            <br/>
            <h2> For Applicants</h2>
            <br/>
            <p>Applicants can easily apply to a wide variety of jobs. No need for lengthy 
                cover letters. Let your resume contents speak for you.
            </p>
            </div>
            
        </React.Fragment>
    )
}

export default About;