/*****************************************************************************/
/* Software Testing Automation Framework (STAF)                              */
/* (C) Copyright IBM Corp. 2002, 2004                                        */
/*                                                                           */
/* This software is licensed under the Eclipse Public License (EPL) V1.0.    */
/*****************************************************************************/

package com.ibm.staf.service.stax;

public class STAXTerminateBlockCondition implements STAXCondition
{
    static final int PRIORITY = 200;

    public STAXTerminateBlockCondition()
    { /* Do Nothing */ }

    public STAXTerminateBlockCondition(String source)
    {
        fSource = source;
    }

    public boolean isInheritable() { return false; }
    public int getPriority() { return PRIORITY; }
    public String getSource() { return fSource; }

    private String fSource = new String("");
}
