#############################################################################
# Software Testing Automation Framework (STAF)                              #
# (C) Copyright IBM Corp. 2006                                              #
#                                                                           #
# This software is licensed under the Eclipse Public License (EPL) V1.0.    #
#############################################################################

# The STAFReturnCodes class defines constants for STAF return codes

class STAFReturnCodes:

    Ok                          = 0
    InvalidAPI                  = 1
    UnknownService              = 2
    InvalidHandle               = 3
    HandleAlreadyExists         = 4
    HandleDoesNotExist          = 5
    UnknownError                = 6
    InvalidRequestString        = 7
    InvalidServiceResult        = 8
    REXXError                   = 9
    BaseOSError                 = 10
    ProcessAlreadyComplete      = 11
    ProcessNotComplete          = 12
    VariableDoesNotExist        = 13
    UnResolvableString          = 14
    InvalidResolveString        = 15
    NoPathToMachine             = 16
    FileOpenError               = 17
    FileReadError               = 18
    FileWriteError              = 19
    FileDeleteError             = 20
    STAFNotRunning              = 21
    CommunicationError          = 22
    TrusteeDoesNotExist         = 23
    InvalidTrustLevel           = 24
    AccessDenied                = 25
    STAFRegistrationError       = 26
    ServiceConfigurationError   = 27
    QueueFull                   = 28
    NoQueueElement              = 29
    NotifieeDoesNotExist        = 30
    InvalidAPILevel             = 31
    ServiceNotUnregisterable    = 32
    ServiceNotAvailable         = 33
    SemaphoreDoesNotExist       = 34
    NotSemaphoreOwner           = 35
    SemaphoreHasPendingRequests = 36
    Timeout                     = 37
    JavaError                   = 38
    ConverterError              = 39
    MoveError                   = 40
    InvalidObject               = 41
    InvalidParm                 = 42
    RequestNumberNotFound       = 43
    InvalidAsynchOption         = 44
    RequestNotComplete          = 45
    ProcessAuthenticationDenied = 46
    InvalidValue                = 47
    DoesNotExist                = 48
    AlreadyExists               = 49
    DirectoryNotEmpty           = 50
    DirectoryCopyError          = 51
    DiagnosticsNotEnabled       = 52
    HandleAuthenticationDenied  = 53
    HandleAlreadyAuthenticated  = 54
    InvalidSTAFVersion          = 55
    RequestCancelled            = 56
    CreateThreadError           = 57
    MaximumSizeExceeded         = 58
    MaximumHandlesExceeded      = 59
    NotRequester                = 60


